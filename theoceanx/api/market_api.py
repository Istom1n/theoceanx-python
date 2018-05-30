import asks
from api_utils import get_endpoint


async def getPairs():
    return await asks.get(get_endpoint('/token_pairs'))


async def getTicker(baseTokenAddress: str, quoteTokenAddress: str):
    return await asks.get(get_endpoint('/ticker',
                                       params={
                                           baseTokenAddress,
                                           quoteTokenAddress
                                       }))


async def getTickers():
    return await asks.get(get_endpoint('/tickers'))


async def getOrderBook(
        baseTokenAddress: str, quoteTokenAddress: str, depth: int):
    return await asks.get(get_endpoint('/order_book',
                                       params={
                                           baseTokenAddress,
                                           quoteTokenAddress,
                                           depth
                                       }))


async def getTradeHistory(baseTokenAddress: str, quoteTokenAddress: str):
    return await asks.get(get_endpoint('/trade_history',
                                       params={
                                           baseTokenAddress,
                                           quoteTokenAddress
                                       }))


async def getCandlesticks(
        baseTokenAddress: str, quoteTokenAddress: str,
        startTime: int, endTime: int, interval: int):
    return await asks.get(get_endpoint('/order_book',
                                       params={
                                           baseTokenAddress,
                                           quoteTokenAddress,
                                           startTime,
                                           endTime,
                                           interval
                                       }))


async def getCandlesticksIntervals():
    return await asks.get(get_endpoint('/candlesticks/intervals'))


async def getOrderInfo(orderHash: str):
    return await asks.get(get_endpoint('/order',
                                       params={
                                           orderHash
                                       }))


async def getAvailableBalance(tokenAddress: str, userAddress: str):
    return await asks.get(get_endpoint('/available_balance',
                                       params={
                                           tokenAddress,
                                           userAddress
                                       }))


async def getCommittedAmounts(tokenAddress: str, walletAddress: str):
    return await asks.get(get_endpoint('/committed_amounts',
                                       params={
                                           tokenAddress,
                                           walletAddress
                                       }))


async def getFeeComponents():
    return await asks.get(get_endpoint('/fee_components'))
