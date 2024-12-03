from UserInputValidator import UserInputValidator

input_data1 = ["abc", "789", "-95", "0.11", "123", "456"]
validatorObject1 = UserInputValidator()

input_data2 = ["0.002", "-789", "95", "11", "123", "xyz"]
validatorObject2 = UserInputValidator()

valid_numbers2 = validatorObject1.validate_positive_integers(input_data2)
print("Valid positive integers of the first initiation:", valid_numbers2)
valid_numbers1 = validatorObject1.validate_positive_integers(input_data1)
print("Valid positive integers of the second initiation:", valid_numbers1)
