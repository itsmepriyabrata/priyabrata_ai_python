from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion_matrix(true_labels, predicted_labels, classes):
    cm = confusion_matrix(true_labels, predicted_labels)
    
    plt.figure(figsize=(len(classes), len(classes)))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=classes, yticklabels=classes)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

# Example usage:
true_labels = [1, 0, 1, 2, 1, 0, 1, 2, 2, 0]
predicted_labels = [1, 0, 1, 2, 1, 0, 2, 2, 2, 0]
class_names = ['Class 0', 'Class 1', 'Class 2']

plot_confusion_matrix(true_labels, predicted_labels, class_names)
