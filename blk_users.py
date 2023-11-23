import gitlab

HOST = '192.168.136.15'
TOKEN = 'glpat-WZrGkg2o11VajcpsDzWP'

gl = gitlab.Gitlab(url=f'http://{HOST}/', private_token=TOKEN)

for row in gl.users.list():
    if(not row.is_admin):
        try:
            gl.users.get(row.id).block()
            print(f'User: {row.username} was blocked.\n')
        except:
            print(f'User: {row.username} was not blocked, error.\n')
    else:
        print(f'User: {row.username} was not blocked, he is admin.\n')
