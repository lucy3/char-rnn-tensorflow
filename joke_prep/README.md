Joke Generator
===

Playing around with [OpenAI's funnybot idea](https://github.com/openai/requests-for-research/blob/master/_requests_for_research/funnybot.html). 

## RNN

Character-level language model created by [sherjilozair](https://github.com/sherjilozair/char-rnn-tensorflow).

Jokes are of variable sequence length, and I filtered out jokes that were too long and added space padding to those that were too short. 

To train in char-rnn-tensorflow directory:

```bash 
python train.py --data_dir=./data/jokes/ trainseq_length=1000
```

Perhaps lucy should read [this](https://github.com/karpathy/char-rnn/issues/47) closely...

## Dataset 

Uses this [joke dataset](https://github.com/taivop/joke-dataset) and [short jokes dataset](https://github.com/amoudgl/short-jokes-dataset). There may be repeats since both datasets scrape from Reddit (e.g. /r/jokes). 

Get joke files:

```bash
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json 
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json
wget https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json 
wget https://raw.githubusercontent.com/amoudgl/short-jokes-dataset/master/shortjokes.csv
```

Many of these jokes are pretty offensive, imo. :(

Then aggregate them into `char-rnn-tensorflow/data/jokes/input.txt`:

```bash
python prep_jokes.py
```

## Results

TODO

## Questions

- Is there a humor neuron, similar to this [sentiment neuron](https://blog.openai.com/unsupervised-sentiment-neuron/)?

## Disclaimer 

I (the human) am still learning, so much of this may be incorrect/bad.
