import tornado.gen
import tornado.web
from common.log import logUtils as log
from common.ripple import userUtils
from common.web import requestsManager
from objects import glob
'''
osu!coins handler made by github.com/SakuruWasTaken
This code was released under the GNU AGPL 3.0, please review the included copy of the licence.
Please do not remove this notice.
'''

MODULE_NAME = "coinsHandler"
class handler(requestsManager.asyncRequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def asyncGet(self):

        ip = self.getRequestIP()
        if not requestsManager.checkArguments(self.request.arguments, ["u", "cs", "action"]):
            return self.write("error: args")

        username = self.get_argument("u")
        password = self.get_argument("cs")

        userID = userUtils.getID(username)
        if userID == 0:
            self.write("error: auth")
            return
        if not userUtils.checkLogin(userID, password, ip):
            self.write("error: auth")
            return
   
        action = self.get_argument("action")
        coinAmountunparsed = glob.db.fetch(f"SELECT coins FROM users WHERE id = {userID}")
        coinAmount = int(coinAmountunparsed["coins"])

        if action == "use":
            glob.db.execute(f"UPDATE users SET coins = coins - 1 WHERE id = {userID};")
        if action == "earn":
            glob.db.execute(f"UPDATE users SET coins = coins + 1 WHERE id = {userID};")
        if action == "recharge":
            glob.db.execute(f"UPDATE users SET coins = 99 WHERE id = {userID};")
        self.write(f"{coinAmount}")
        return



