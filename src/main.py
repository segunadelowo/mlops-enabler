import argparse
import sys
from preprocess import categorical

def run_training() -> None:
    """Train the model."""
    data_preprocessing()
    split_data()
    fit_and_save_model()
    predict_test()
    measure_model_performance()


def data_preprocessing():
    print("data_preprocessing...OK.")
    pass


def split_data():
    print("split_data...OK.")
    pass


def fit_and_save_model():
    print("fit_and_save_model...OK.")
    pass


def predict_test():
    print("predict_test...OK.")
    pass


def measure_model_performance():
    print("measure_model_performance...OK.")
    pass

def load_data():
    print("load_data...OK.")
    pass

def validate():
    print("validate...OK. "+ categorical.test())
    pass

def extract_features():
    print("extract_features...OK.")
    pass

def cache_features():
    print("cache_features...OK.")
    pass

if __name__ == "__main__":
    # run_training()
    # run_prediction()
    #data_preprocessing()
    #split_data()
    #fit_and_save_model()
    #predict_test()
    #measure_model_performance()
    

    parser = argparse.ArgumentParser(description='Process step')
    parser.add_argument('task', type=str, help='task to be done')
    args = parser.parse_args()
    if args.task == 'load_data':
        load_data()
    elif args.task == 'validate':
        validate()
    elif args.task == 'extract_features':
        extract_features()
    elif args.task == 'cache_features':
        cache_features()
    else:
        raise ValueError('Invalid entry')
        #sys.exit(0)

    '''
    args = parser.parse_args()
    print(args.task) 
    match "validate":
        case "load_data":
            load_data()
        case "validate":
            validate()
        case "extract_features":
            extract_features()
        case _:
            sys.exit(1)
    '''