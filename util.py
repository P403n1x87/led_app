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

import os
PATH = os.path.dirname(__file__)

from cgi import parse_qs, escape

def qs(env):
    return parse_qs(env.get('QUERY_STRING', ''))

def templ(name, *args, **kwargs):
    """
    Returns a formatted HTML template
    """

    with open(os.path.join(PATH, name + ".html")) as fin:
        return fin.read().format(*args, **kwargs)
