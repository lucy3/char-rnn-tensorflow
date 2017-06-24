Joke Generator
===

Playing around with [OpenAI's funnybot idea](https://github.com/openai/requests-for-research/blob/master/_requests_for_research/funnybot.html). 

## RNN

Character-level language model created by [sherjilozair](https://github.com/sherjilozair/char-rnn-tensorflow).

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
