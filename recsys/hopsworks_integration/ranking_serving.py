import os

import joblib
from hsml.transformer import Transformer

from recsys.config import settings


class HopsworksRankingModel:
    deployment_name = "ranking"

    def __init__(self, model):
        self._model = model

    def save_to_local(self, output_path: str = "ranking_model.pkl"):
        joblib.dump(self._model, output_path)

        return output_path

    def register(self, mr, feature_view, X_train, metrics):
        local_model_path = self.save_to_local()

        input_example = X_train.sample().to_dict("records")

        ranking_model = mr.python.create_model(
            name="ranking_model",
            description="Ranking model that scores item candidates",
            metrics=metrics,
            input_example=input_example,
            feature_view=feature_view,
        )
        ranking_model.save(local_model_path)

    @classmethod
    def deploy(cls, project):
        mr = project.get_model_registry()
        dataset_api = project.get_dataset_api()

        ranking_model = mr.get_best_model(
            name="ranking_model",
            metric="fscore",
            direction="max",
        )

        # Copy transformer file into Hopsworks File System
        uploaded_file_path = dataset_api.upload(
            str(
                settings.RECSYS_DIR / "inference" / "ranking_transformer.py"
            ),  # File name to be uploaded
            "Resources",  # Destination directory in Hopsworks File System
            overwrite=True,  # Overwrite the file if it already exists
        )
        # Construct the path to the uploaded transformer script
        transformer_script_path = os.path.join(
            "/Projects",  # Root directory for projects in Hopsworks
            project.name,  # Name of the current project
            uploaded_file_path,  # Path to the uploaded file within the project
        )

        # Upload predictor file to Hopsworks
        uploaded_file_path = dataset_api.upload(
            str(settings.RECSYS_DIR / "inference" / "ranking_predictor.py"),
            "Resources",
            overwrite=True,
        )

        # Construct the path to the uploaded script
        predictor_script_path = os.path.join(
            "/Projects",
            project.name,
            uploaded_file_path,
        )

        ranking_transformer = Transformer(
            script_file=transformer_script_path,
            resources={"num_instances": 0},
        )

        # Deploy ranking model
        ranking_deployment = ranking_model.deploy(
            name=cls.deployment_name,
            description="Deployment that search for item candidates and scores them based on customer metadata",
            script_file=predictor_script_path,
            resources={"num_instances": 0},
            transformer=ranking_transformer,
        )

        return ranking_deployment