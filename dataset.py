from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "abrahamkevan/supermarket-sales",
    path="datasets",
    unzip=True
)

print("DATASET BAIXADO 🚀")