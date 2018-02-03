import hug
import hook

@hug.cli()
@hug.get(examples='name=tolgahanuzun')
def user_details(name: hug.types.text, hug_timer=3):
    """User Details"""
    return {'result': hook.hook(name),
            'took': float(hug_timer)}

if __name__ == '__main__':
    happy_birthday.interface.cli()