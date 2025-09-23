from hsfs.feature import Feature

### Post ingestion format.###

customer_feature_descriptions = [
    {"name": "customer_id", "description": "Unique identifier for each customer."},
    {
        "name": "club_member_status",
        "description": "Membership status of the customer in the club.",
    },
    {"name": "age", "description": "Age of the customer."},
    {
        "name": "postal_code",
        "description": "Postal code associated with the customer's address.",
    },
    {"name": "age_group", "description": "Categorized age group of the customer."},
]

transactions_feature_descriptions = [
    {"name": "t_dat", "description": "Timestamp of the data record."},
    {"name": "customer_id", "description": "Unique identifier for each customer."},
    {"name": "article_id", "description": "Identifier for the purchased article."},
    {"name": "price", "description": "Price of the purchased article."},
    {"name": "sales_channel_id", "description": "Identifier for the sales channel."},
    {"name": "year", "description": "Year of the transaction."},
    {"name": "month", "description": "Month of the transaction."},
    {"name": "day", "description": "Day of the transaction."},
    {"name": "day_of_week", "description": "Day of the week of the transaction."},
    {
        "name": "month_sin",
        "description": "Sine of the month used for seasonal patterns.",
    },
    {
        "name": "month_cos",
        "description": "Cosine of the month used for seasonal patterns.",
    },
]

interactions_feature_descriptions = [
    {"name": "t_dat", "description": "Timestamp of the interaction."},
    {"name": "customer_id", "description": "Unique identifier for each customer."},
    {
        "name": "article_id",
        "description": "Identifier for the article that was interacted with.",
    },
    {
        "name": "interaction_score",
        "description": "Type of interaction: 0 = ignore, 1 = click, 2 = purchase.",
    },
    {
        "name": "prev_article_id",
        "description": "Previous article that the customer interacted with, useful for sequential recommendation patterns.",
    },
]

ranking_feature_descriptions = [
    {"name": "customer_id", "description": "Unique identifier for each customer."},
    {"name": "article_id", "description": "Identifier for the purchased article."},
    {"name": "age", "description": "Age of the customer."},
    {"name": "product_type_name", "description": "Name of the product type."},
    {"name": "product_group_name", "description": "Name of the product group."},
    {
        "name": "graphical_appearance_name",
        "description": "Name of the graphical appearance.",
    },
    {"name": "colour_group_name", "description": "Name of the colour group."},
    {
        "name": "perceived_colour_value_name",
        "description": "Name of the perceived colour value.",
    },
    {
        "name": "perceived_colour_master_name",
        "description": "Name of the perceived colour master.",
    },
    {"name": "department_name", "description": "Name of the department."},
    {"name": "index_name", "description": "Name of the index."},
    {"name": "index_group_name", "description": "Name of the index group."},
    {"name": "section_name", "description": "Name of the section."},
    {"name": "garment_group_name", "description": "Name of the garment group."},
    {
        "name": "label",
        "description": "Label indicating whether the article was purchased (1) or not (0).",
    },
]

### Pre ingestion format. ###

article_feature_description = [
    Feature(
        name="article_id", type="string", description="Identifier for the article."
    ),
    Feature(
        name="product_code",
        type="bigint",
        description="Code associated with the product.",
    ),
    Feature(name="prod_name", type="string", description="Name of the product."),
    Feature(
        name="product_type_no",
        type="bigint",
        description="Number associated with the product type.",
    ),
    Feature(
        name="product_type_name", type="string", description="Name of the product type."
    ),
    Feature(
        name="product_group_name",
        type="string",
        description="Name of the product group.",
    ),
    Feature(
        name="graphical_appearance_no",
        type="bigint",
        description="Number associated with graphical appearance.",
    ),
    Feature(
        name="graphical_appearance_name",
        type="string",
        description="Name of the graphical appearance.",
    ),
    Feature(
        name="colour_group_code",
        type="bigint",
        description="Code associated with the colour group.",
    ),
    Feature(
        name="colour_group_name", type="string", description="Name of the colour group."
    ),
    Feature(
        name="perceived_colour_value_id",
        type="bigint",
        description="ID associated with perceived colour value.",
    ),
    Feature(
        name="perceived_colour_value_name",
        type="string",
        description="Name of the perceived colour value.",
    ),
    Feature(
        name="perceived_colour_master_id",
        type="bigint",
        description="ID associated with perceived colour master.",
    ),
    Feature(
        name="perceived_colour_master_name",
        type="string",
        description="Name of the perceived colour master.",
    ),
    Feature(
        name="department_no",
        type="bigint",
        description="Number associated with the department.",
    ),
    Feature(
        name="department_name", type="string", description="Name of the department."
    ),
    Feature(
        name="index_code", type="string", description="Code associated with the index."
    ),
    Feature(name="index_name", type="string", description="Name of the index."),
    Feature(
        name="index_group_no",
        type="bigint",
        description="Number associated with the index group.",
    ),
    Feature(
        name="index_group_name", type="string", description="Name of the index group."
    ),
    Feature(
        name="section_no",
        type="bigint",
        description="Number associated with the section.",
    ),
    Feature(name="section_name", type="string", description="Name of the section."),
    Feature(
        name="garment_group_no",
        type="bigint",
        description="Number associated with the garment group.",
    ),
    Feature(
        name="garment_group_name",
        type="string",
        description="Name of the garment group.",
    ),
    Feature(
        name="prod_name_length",
        type="bigint",
        description="Length of the product name.",
    ),
    Feature(
        name="article_description",
        type="string",
        online_type="VARCHAR(5800)",
        description="Description of the article.",
    ),
    Feature(
        name="embeddings",
        type="array<double>",
        description="Vector embeddings of the article description.",
    ),
    Feature(name="image_url", type="string", description="URL of the product image."),
]