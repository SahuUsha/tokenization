import tiktoken 

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab_Size : ",encoder.n_vocab)

text="we are gen-ai developer"
token = encoder.encode(text)
print(token)

my_token = [854, 553, 3645, 159269, 24261]
decoded = encoder.decode(my_token)
print("Decoded : ",decoded)