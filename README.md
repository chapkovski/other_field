# An example of 'Other' field usage in oTree

This code provides a basic field to let the user choose between a set 
of choices (rendered as a set of radio buttons), plus an extra 'Other' option.

If a user chooses 'Other' option, the extra text input is provided, where they
can insert an answer.

## Installation

1. Copy `fields.py` and `widgets.py` to your app folder (where `models.py` and
'pages.py` are located).
2. Copy `templates/widgets` folder to a `templates` folder of your app.
3. In your `models.py` import `OtherModelField` and use it in your models:

```python
from .fields import OtherModelField


class Player(BasePlayer):
    ddd = OtherModelField(label='Who should be the next German soccer team coach?',
                          choices=['Donald Trump', 'Vladimir Putin', 'Arnold Schwarzenegger'],
                          )
``` 

If a user chooses one of the options in `choices` of your field the value stored
will be the one he chooses (in the example above, for instance "Donald Trump")
if a user chooses the first option.

If they choose the 'Other' option, then the value stored will look like:
_other: THEIR ANSWER_

You can define two extra parameters:

* `other_label`: that changes how the 'Other' option look like. 
    _default:_ 'Other'
* `other_value`: that changes how that marker that is added to the 
beginning of user answer look like. _default:_ 'other' 

