# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
from tqdm import tqdm
import utils
eval_corpus_path = "birth_test_inputs.tsv"
with open(eval_corpus_path, encoding='utf-8') as fin:
    lines = [x.strip().split('\t') for x in fin]
predictions = ["London" for line in lines]
total, correct = utils.evaluate_places(eval_corpus_path, predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
