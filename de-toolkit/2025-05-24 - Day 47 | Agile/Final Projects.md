# Final Project
## Kyle's recommendations
- Give yourself One Goal
- Consider any gaps in your knowledge at this point.
- Give yourself a development goal.
- Acknowledge the aim of the next phase of the bootcamp is consolidation of learning, not product production.
- Understand that progress together as a team is more valuable than a subset of the team delivering a polished outcome.
- Understand that staying in your comfort zone will only make it harder after graduation.

## Questions
- what github repo?
- which kanban
- 
CI/CD First
- formatting
- quality
- 

Suggestions:
- Create user stories

- A common function api interface and return value:
    - semantic function names:
        - get_s3_object
        - create_s3_object
        - list_s3_objects
        - delete_s3_object
        - update_s3_object
    - return values:
    Each key/value pair is optional except for `success` and `error` but inside `success` or `error` there should not be anything other than `message`, `data`, `status_code` or `raw_response`,
```python
{
    'success': {
        'data':{
            'some_key': 'some value'
            'another_key': 'another value'
        }
        'status_code': 123
        'message': 'Some message!!'
        'raw_response': {'dadadada':'tatata'}
    }
}
```
OR
```python
{
    'error': {
        'status_code': 456
        'message': 'Error: Error description!!'
        'raw_response': {'dadadada':'tatata'}
    }
}
```

