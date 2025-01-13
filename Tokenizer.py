from transformers import BertModel ,BertTokenizer

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = tokenizer.tokenize(input('Enter Sentence: '))

print(sentence)


