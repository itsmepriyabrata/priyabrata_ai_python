import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class IMDbReviewClassifier:
    def _init_(self, model_name='distilbert-base-uncased', max_length=512, batch_size=8, epochs=3):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_name)
        self.max_length = max_length
        self.batch_size = batch_size
        self.epochs = epochs

    def preprocess_data(self, reviews, labels):
        input_ids = []
        attention_masks = []

        for review in reviews:
            encoding = self.tokenizer(
                review,
                truncation=True,
                max_length=self.max_length,
                padding='max_length',
                return_tensors='pt'
            )

            input_ids.append(encoding['input_ids'])
            attention_masks.append(encoding['attention_mask'])

        input_ids = torch.cat(input_ids, dim=0)
        attention_masks = torch.cat(attention_masks, dim=0)
        labels = torch.tensor(labels)

        return input_ids, attention_masks, labels

    def train_model(self, train_data, train_labels):
        input_ids, attention_masks, labels = self.preprocess_data(train_data, train_labels)
        dataset = torch.utils.data.TensorDataset(input_ids, attention_masks, labels)
        train_loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)

        optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5)

        for epoch in range(self.epochs):
            self.model.train()
            for batch in train_loader:
                optimizer.zero_grad()
                inputs, masks, labels = batch
                outputs = self.model(inputs, attention_mask=masks, labels=labels)
                loss = outputs.loss
                loss.backward()
                optimizer.step()

    def evaluate_model(self, test_data, test_labels):
        input_ids, attention_masks, labels = self.preprocess_data(test_data, test_labels)
        dataset = torch.utils.data.TensorDataset(input_ids, attention_masks, labels)
        test_loader = DataLoader(dataset, batch_size=self.batch_size)

        self.model.eval()
        predictions = []

        with torch.no_grad():
            for batch in test_loader:
                inputs, masks, _ = batch
                outputs = self.model(inputs, attention_mask=masks)
                logits = outputs.logits
                predictions.extend(torch.argmax(logits, dim=1).tolist())

        accuracy = accuracy_score(test_labels, predictions)
        return accuracy

# Example usage:
train_reviews = ["Great movie!", "Terrible plot."]
train_labels = [1, 0]  # 1 for positive, 0 for negative

test_reviews = ["Amazing film!", "Waste of time."]
test_labels = [1, 0]

classifier = IMDbReviewClassifier()
classifier.train_model(train_reviews, train_labels)
accuracy = classifier.evaluate_model(test_reviews, test_labels)
print(f"Accuracy on test data: {accuracy}")
