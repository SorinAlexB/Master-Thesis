def runner(model_api :str = None, dataset_path :str = None, dataset_sample :str = None) -> bool:
    if model_api is None:
        raise ValueError("Model API path not mentioned!")
    elif dataset_path is not None and dataset_sample is not None:
        raise ValueError("dataset_path and dataset_sample can't be defined at the same time!")
    elif dataset_path is None and dataset_sample is None:
        raise ValueError("dataset_path and dataset_sample can't be None at the same time!")
    else:
        # start testing for MIA methods and information retentantion 
        None
    return False

if __name__ == "__main__":
    rc = runner()
    if rc is False:
        raise RuntimeError("PEP module returned without execution!")