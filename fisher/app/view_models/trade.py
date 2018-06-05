#此文件写的是gift和wish共同有的详情东西
from app.view_models.book import BookViewModel


class TradeInfo :
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nick_name,
            time=time,
            id=single.id
        )

class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            # for wish_count in self.__wish_count_list:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:  # 这几行代码参照models里的gift模型中的方法
                count = trade_count['count']

        r = {
            'wishes_count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return r
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift
