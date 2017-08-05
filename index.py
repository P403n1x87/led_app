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

from util import templ, qs
from led  import LED

led = LED(15)

class Index(object):

    @staticmethod
    def main(env):
        params = qs(env)
        if "action" in params and 'toggle' in params['action']:
            led.toggle()
        return templ('index', state = "on" if led.state else "off")
