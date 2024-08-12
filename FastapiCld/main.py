
from fastapi import FastAPI

app     = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

"""
@app.post('/get_CarInfo')
async def get_CarInfo(file:UploadFile):
     image = await file.read()
     image_np_array = np.frombuffer(image, np.uint8)
     image = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)
     car_Info = carInfo(image)
     return car_Info
"""

     