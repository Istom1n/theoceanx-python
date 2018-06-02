from api_utils import get_endpoint
from asks import Response, get


async def get_pairs():
    return await get(get_endpoint('/token_pairs'))


async def get_ticker(
        baseTokenAddress: str,
        quoteTokenAddress: str
) -> Response:
    return await get(
        get_endpoint(
            '/ticker',
            params={
                baseTokenAddress,
                quoteTokenAddress
            }
        )
    )


async def get_tickers() -> Response:
    return await get(get_endpoint('/tickers'))


async def get_order_book(
        baseTokenAddress: str,
        quoteTokenAddress: str,
        depth: int
) -> Response:
    return await get(
        get_endpoint(
            '/order_book',
            params={
                baseTokenAddress,
                quoteTokenAddress,
                depth
            }
        )
    )


async def get_trade_history(
        baseTokenAddress: str,
        quoteTokenAddress: str
) -> Response:
    return await get(
        get_endpoint(
            '/trade_history',
            params={
                baseTokenAddress,
                quoteTokenAddress
            }
        )
    )


async def get_candlesticks(
        baseTokenAddress: str,
        quoteTokenAddress: str,
        startTime: int,
        endTime: int,
        interval: int
) -> Response:
    return await get(
        get_endpoint(
            '/order_book',
            params={
                baseTokenAddress,
                quoteTokenAddress,
                startTime,
                endTime,
                interval
            }
        )
    )


async def get_candlesticks_intervals() -> Response:
    return await get(get_endpoint('/candlesticks/intervals'))


async def get_order_info(orderHash: str):
    return await get(
        get_endpoint(
            '/order',
            params={
                orderHash
            }
        )
    )


async def get_available_balance(
        tokenAddress: str,
        userAddress: str
) -> Response:
    return await get(
        get_endpoint(
            '/available_balance',
            params={
                tokenAddress,
                userAddress
            }
        )
    )


async def get_committed_amounts(
        tokenAddress: str,
        walletAddress: str
) -> Response:
    return await get(
        get_endpoint(
            '/committed_amounts',
            params={
                tokenAddress,
                walletAddress
            }
        )
    )


async def get_fee_components() -> Response:
    return await get(get_endpoint('/fee_components'))
