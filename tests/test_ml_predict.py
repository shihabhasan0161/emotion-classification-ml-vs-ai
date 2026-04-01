import api


class DummyVectorizer:
    def transform(self, texts):
        return texts


class DummyModel:
    def __init__(self, prediction):
        self.prediction = prediction

    def predict(self, vec):
        return [self.prediction]


def test_predict_returns_expected_label(test_client, monkeypatch):
    monkeypatch.setattr(api, "preprocess_text", lambda text: text.lower())
    monkeypatch.setattr(api, "vectorizer", DummyVectorizer())
    monkeypatch.setattr(api, "model", DummyModel(1))

    response = test_client.post("/predict", json={"message": "I am so happy today!"})

    assert response.status_code == 200
    assert response.get_json() == {"Model Prediction": 1}


def test_predict_supports_alternate_prediction_value(test_client, monkeypatch):
    monkeypatch.setattr(api, "preprocess_text", lambda text: text.lower())
    monkeypatch.setattr(api, "vectorizer", DummyVectorizer())
    monkeypatch.setattr(api, "model", DummyModel(0))

    response = test_client.post("/predict", json={"message": "I am sad."})

    assert response.status_code == 200
    assert response.get_json() == {"Model Prediction": 0}