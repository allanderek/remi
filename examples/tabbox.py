"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):

        b1 = gui.Button('Show second tab', width=200, height=30)
        
        tb = gui.TabBox(width='80%')
        tb.add_tab(b1, 'First', None)

        b2 = gui.Button('Second Button', width=200, height=30)
        tb.add_tab(b2, 'Second', None)

        b3 = gui.Button('Third Button', width=200, height=30)
        tb.add_tab(b3, 'Third', None)
        
        b1.set_on_click_listener(self.on_bt1_pressed, tb, b2)

        return tb

    def on_bt1_pressed(self, widget, tabbox, refWidgetTab):
        tabbox.show_tab(refWidgetTab)
    
if __name__ == "__main__":
    start(MyApp, title="Tab Demo", standalone=False)
