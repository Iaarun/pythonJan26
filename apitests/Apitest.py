from playwright.sync_api import sync_playwright, expect


def test_get_API():
    with sync_playwright() as p:
     request=  p.request.new_context()
     response = request.get("http://localhost:3000/products")
     print(type(response.status))
     assert response.status == 200
     print(response.json())

def test_get_singleproduct():
    with sync_playwright() as p:
     request=  p.request.new_context()
     response = request.get("http://localhost:3000/products/13")
     print(type(response.status))
     assert response.status == 200
     print(response.json())
     assert response.json()["id"] == 13
     assert response.json()["category"] == "Electronics"


paylod= """{
    "title": "Iphone",
    "price": 109.95,
    "description": "New upgraded for your everyday work",
    "category": "Electronics",
    "image": "https://fakestoreapi.com/img/iphone.png",
    "rating": {
        "rate": 3.9,
        "count": 120
    }
}"""

def test_createproduct():
    with sync_playwright() as p:
     request=  p.request.new_context()
     response = request.post("http://localhost:3000/products",data=paylod, headers={"Content-Type": "application/json"})
     print(type(response.status))
     assert response.status == 201
     print(response.json())
     assert response.json()["title"] == "Iphone"
     assert response.json()["category"] == "Electronics"
     assert response.json()["rating"]["count"]==120