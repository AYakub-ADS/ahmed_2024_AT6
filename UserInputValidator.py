class UserInputValidator:
    """A class to validate user inputs."""
    @staticmethod
    def validated_message():
        print("List validated successfully.")

    @staticmethod
    def validate_positive_integers(input_list):
        """
        Validates a list of strings and returns a list of valid positive integers.

        Parameters:
            input_list (list): A list of strings to validate.

        Returns:
            list: A list of valid positive integers.
        """
        valid_integers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_integers.append(int(item))
        UserInputValidator.validated_message()
        return valid_integers

