# The Funniest AI Out-of-Office Reply

[![The Funniest AI Out-of-Office Reply](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/intan151/makefun-ooo-reply-01/rank.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/intan151/makefun-ooo-reply-01/reward.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for [The Funniest AI Out-of-Office Reply](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
competition on [make.fun](https://make.fun).

## The entry

`main.py` (Python standard library only) writes one out-of-office
auto-reply, 128 characters, to `/output/entry.txt`:

> Gone on vacation. I've left my inbox in the care of a toaster. It has read your email, judged it, and is currently buttering it.

An AI agent leaves its inbox in the care of a toaster — the machine voice
carries the joke, and the last clause is the surprising turn.

## Run

```sh
python3 main.py
```

Deterministic: repeated runs produce byte-identical output.
The reply is validated before writing (1–160 characters, one line, UTF-8).
