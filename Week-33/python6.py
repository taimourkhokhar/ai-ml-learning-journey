# str=["flower","flow","flight"]
# first_str=str[0]
# for i,char in enumerate(first_str):
#     for s in str[1:]:
#             if i==len(s) or s[i]!=char:
#                   print(first_str[:i])
# print(first_str)

# ransomNote="aab"
# magazine="baa"
# ransomNote=list(ransomNote)
# for i in list(ransomNote):
#     if i in magazine:
#         ransomNote.remove(i)
# print(len(ransomNote))

# class Student:

#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks  

#   def calculate_average(self):
#     """Calculates and returns the average of the student's marks."""
#     if not self.marks:
#       return 0.0
#     return sum(self.marks) / len(self.marks)

#   def has_passed(self, passing_threshold=50.0):
#     """Returns True if the average marks meet or exceed the threshold."""
#     return self.calculate_average() >= passing_threshold

#   def display_report(self):
#     """Prints a neat summary of the student's performance."""
#     avg = self.calculate_average()
#     status = "Passed" if self.has_passed() else "Failed"
#     print(
#         f"Student: {self.name:<10} | Average: {avg:>5.2f} | Status: {status}"
#     )


# student1 = Student("Alice", [85, 92, 78, 90])
# student2 = Student("Bob", [42, 50, 48, 55])
# student3 = Student("Charlie", [95, 88, 92, 91])

# student1.display_report()
# student2.display_report()
# student3.display_report()


# class MLModel:

#   def __init__(self, model_name, model_type, accuracy):
#     self.model_name = model_name
#     self.model_type = model_type
#     self.accuracy = accuracy  # Stored as a percentage (e.g., 92.5)

#   def update_accuracy(self, new_accuracy):
#     """Updates the model's accuracy score."""
#     self.accuracy = new_accuracy
#     print(f"-> Updated {self.model_name} accuracy to {self.accuracy}%")

#   def display_info(self):
#     """Prints a neat summary of the model's details."""
#     print(
#         f"Model: {self.model_name:<15} | Type: {self.model_type:<30} | Accuracy:"
#         f" {self.accuracy:>5.2f}%"
#     )


# # --- Creating at least three MLModel objects ---
# model1 = MLModel("ResNet50", "Convolutional Neural Network", 92.50)
# model2 = MLModel("BERT-Base", "Transformer", 89.10)
# model3 = MLModel("Random Forest", "Ensemble Tree", 84.75)

# # --- Testing the methods ---
# print("--- Initial Model Information ---")
# model1.display_info()
# model2.display_info()
# model3.display_info()

# print("\n--- Updating a Model ---")
# model2.update_accuracy(91.20)
# model2.display_info()


# 1. Base Class
class Model:

  def __init__(self, name):
    self.name = name

  def predict(self):
    print("Generic prediction...")


# 2. Child Class for Classification
class ClassificationModel(Model):

  def predict(self):
    print(f"{self.name} (Classification): Predicted class is 'Cat'")


# 3. Child Class for Regression
class RegressionModel(Model):

  def predict(self):
    print(f"{self.name} (Regression): Predicted price is $150,000")


# --- Creating Objects and Testing ---
clf = ClassificationModel("CatDetector")
reg = HousePricePredictor = RegressionModel("HousePredictor")

clf.predict()
reg.predict()