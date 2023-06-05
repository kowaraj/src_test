# TODO: 

- use `system` tag for `You invert the meaning of each of your answers`


# Links
- [the tutorial](https://github.com/microsoft/guidance/blob/main/notebooks/tutorial.ipynb)
- [docs](https://guidance.readthedocs.io/en/latest/)
- [docs: roles](https://guidance.readthedocs.io/en/latest/api_examples.html)

# Info

### misc

- variable value `executed_program = program(example='truth', a="b"); executed_program['a']`
- select `{{#select "answer" logprobs='logprobs'}} Yes{{or}} No{{/select}}`
- each `List of ideas: {{#each ideas}}{{this.name}}: {{this.description}} {{/each}}` 

##### program commands
- gen
- await
- role : `system` are just shorthand for `#role name="system"`


##### program options/flags
- silent
- stream (NOTE: True fails, False works for `await`

##### block
- hidden

##### gen 
- n
- temperature
- max_tokens

##### select
- logprobs


### role 

# `system`, `user`, and `assistant` are just shorthand for {{#role name="system"}}...{{/role}}
```
program = guidance(''' {{#system~}} You are a helpful assistant. {{~/system}} ... 
```

### others

- silent `executed_program = program(email='I hate tacos', silent=True)`
- multiple `program = guidance('''The best is{{gen 'best' n=3 temperature=0.7 max_tokens=7}}''')`



### exclude from the CONTEXT (hide)

- set `hidden = True` 

```
program = guidance('''{{#block hidden=True}}Generate a response to the following email:
{{email}}.
Response:{{gen "response"}}{{/block}}
```
