def get_mongodb_url():
    local_url="mongodb://localhost:27017/"
    cloud_url="mongodb+srv://hemanth:hemanth@cluster0.xuuie.mongodb.net/CriminalDetectionSystem?retryWrites=true&w=majority"
    return cloud_url

# Other config functions here
def get_haar_cascade_path():
    haar_cascade_path = r"C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\Resources\HaarCascadeFiles\haarcascade_frontalface_default.xml"
    return haar_cascade_path
def get_storage_path():
    storage_path=r"C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\Resources\storage"
    return storage_path

def get_trained_model_path_folder():
    trained_model_path_folder = r"C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\trained_model"
    return trained_model_path_folder

def get_trained_model_path():
    trained_model_path = r"C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\trained_model\face_trained.yml"
    return trained_model_path

def get_bg_image_url():
    return r'C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\Resources\images\login.jpg'


def get_criminal_labels():
    criminals = ["18H61A05J4","18H61A05K1","18H61A05M0","18H61A05M3","18H61A05N5","18H61A05N6","18H61A05N7","19H65A0520","nandini","sowmya"]
    return criminals
