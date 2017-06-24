Joke Generator
===

Playing around with [OpenAI's funnybot idea](https://github.com/openai/requests-for-research/blob/master/_requests_for_research/funnybot.html). 

## RNN

Character-level language model created by [sherjilozair](https://github.com/sherjilozair/char-rnn-tensorflow).

Jokes are of variable sequence length. In the input file I'm adding padding so that all of the jokes are the same length, and I use the seq_length argument to indicate this length. I guess when I sample for characters I'll have to say I want this number of characters as well... 

Perhaps lucy should read [this](https://github.com/karpathy/char-rnn/issues/47) closely...

## Dataset 

Uses this [joke dataset](https://github.com/taivop/joke-dataset). 

Get joke jsons:
```bash
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json 
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json 
```

Many of these jokes are pretty offensive, imo. :(

## TODO

[ ] Convert jsons to one input txt w/ good jokes

[ ] GANs???

## Questions

- Is there a humor neuron, similar to this [sentiment neuron](https://blog.openai.com/unsupervised-sentiment-neuron/)?

## Disclaimer 

I (the human) am still learning.
