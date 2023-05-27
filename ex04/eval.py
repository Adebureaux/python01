class Evaluator:
	@staticmethod
	def zip_evaluate(words, coefs):
		if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
			raise ValueError("zip_evaluate error: words should be a list of string.")
		if not isinstance(coefs, list) or not all(isinstance(coef, (int, float)) for coef in coefs):
			raise ValueError("zip_evaluate error: coefs should be a list of integers or floats.")
		if (len(words) != len(coefs)):
			return -1
		result = 0
		for word, coef in zip(words, coefs):
			result += len(word) * coef
		return result

	@staticmethod
	def enumerate_evaluate(words, coefs):
		if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
			raise ValueError("enumerate_evaluate error: words should be a list of string.")
		if not isinstance(coefs, list) or not all(isinstance(coef, (int, float)) for coef in coefs):
			raise ValueError("enumerate_evaluate error: coefs should be a list of integers or floats.")
		if (len(words) != len(coefs)):
			return -1
		result = 0
		for i, word in enumerate(words):
			result += len(word) * coefs[i]
		return result