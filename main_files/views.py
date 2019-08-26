from aiohttp import web
import aiohttp_jinja2
import requests
import json
from main_files.settings import MY_BOOKS_URL
from aiohttp_session import get_session


@aiohttp_jinja2.template('base.html')
async def base(request):
    return


def qwe():
    asd = 123
    return asd


async def books(request):
    print(str(request))
    context = dict()
    session = await get_session(request)
    my_book_cookies = session.get('my_book_cookies', None)
    # print('my_book_cookies=', my_book_cookies)
    if my_book_cookies:
        response = requests.get(MY_BOOKS_URL + 'api/profile/', cookies=session.get('my_book_cookies'))
        text = json.loads(response.text)
        bookuserlist_response = requests.get(
            MY_BOOKS_URL + 'api/bookuserlist/?user=' + str(text['objects'][0]['id']),
            cookies=session.get('my_book_cookies')
        )
        items = bookuserlist_response.json()['objects']
        context['items'] = items
    return web.json_response(context)


class Authentication(web.View):
    authentication_url = 'api/auth/'

    async def post(self):
        data = await self.request.post()
        response = requests.post(
            MY_BOOKS_URL + self.authentication_url,
            data={"email": data.get('email', ''), "password":  data.get('password', '')}
        )
        session = await get_session(self.request)
        session['my_book_cookies'] = dict(response.cookies)
        return web.Response()

    async def get(self):
        session = await get_session(self.request)
        if session.get('my_book_cookies', None):
            session = await get_session(self.request)
            response = requests.get(MY_BOOKS_URL + 'api/profile/', cookies=session.get('my_book_cookies'))
            return web.Response(text=str(json.loads(response.text)['objects'][0]['email']))
        return web.Response(status=404)

    async def delete(self):
        session = await get_session(self.request)
        if session.get('my_book_cookies', None):
            session['my_book_cookies'] = None
            return web.Response()
        return web.Response(status=418)
