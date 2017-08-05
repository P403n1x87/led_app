# This file is part of "led_app" which is released under GPL.
# See file LICENCE or go to http://www.gnu.org/licenses/ for full license
# details.
#
# Copyright (c) 2017 Gabriele N. Tornetta <phoenix1987@gmail.com>. All rights
# reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os
sys.path.append(os.path.dirname(__file__))

from index import Index

def main(env, start_response):
    status = '200 OK'

    output = Index.main(env)

    response_headers = [
        ('Content-type'   , 'text/html'     )
       ,('Content-Length' , str(len(output)))
    ]
    start_response(status, response_headers)

    return [output]

from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(main, debug=True)
