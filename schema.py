import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.dataset as ds

from pyarrow import int64, timestamp, float64, decimal128, string, date32, date64
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.functions import *
from pyspark.sql.types import TimestampType
from pyspark.sql.window import Window
from pyspark.sql.types import *

fixed_taq_min = pa.schema([
    ("Date", int64()),
    ("BarDateTime", timestamp('ns', tz='America/New_York')),
    ("Ticker", string()),
    ("OpenBarTimeOffset", float64()),
    ("OpenBidPrice", float64()),
    ("OpenBidSize", int64()),
    ("OpenAskPrice", float64()),
    ("OpenAskSize", int64()),
    ("FirstTradeTimeOffset", float64()),
    ("FirstTradePrice", float64()),
    ("FirstTradeSize", int64()),
    ("HighBidTimeOffset", float64()),
    ("HighBidPrice", float64()),
    ("HighBidSize", int64()),
    ("HighAskTimeOffset", float64()),
    ("HighAskPrice", float64()),
    ("HighAskSize", int64()),
    ("HighTradeTimeOffset", float64()),
    ("HighTradePrice", float64()),
    ("HighTradeSize", int64()),
    ("LowBidTimeOffset", float64()),
    ("LowBidPrice", float64()),
    ("LowBidSize", int64()),
    ("LowAskTimeOffset", float64()),
    ("LowAskPrice", float64()),
    ("LowAskSize", int64()),
    ("LowTradeTimeOffset", float64()),
    ("LowTradePrice", float64()),
    ("LowTradeSize", int64()),
    ("CloseBarTimeOffset", float64()),
    ("CloseBidPrice", float64()),
    ("CloseBidSize", int64()),
    ("CloseAskPrice", float64()),
    ("CloseAskSize", int64()),
    ("LastTradeTimeOffset", float64()),
    ("LastTradePrice", float64()),
    ("LastTradeSize", int64()),
    ("MinSpread", float64()),
    ("MaxSpread", float64()),
    ("CancelSize", int64()),
    ("VolumeWeightPrice", float64()),
    ("NBBOQuoteCount", int64()),
    ("TradeAtBid", int64()),
    ("TradeAtBidMid", int64()),
    ("TradeAtMid", int64()),
    ("TradeAtMidAsk", int64()),
    ("TradeAtAsk", int64()),
    ("TradeAtCrossOrLocked", int64()),
    ("Volume", int64()),
    ("TotalTrades", int64()),
    ("FinraVolume", int64()),
    ("FinraVolumeWeightPrice", float64()),
    ("UptickVolume", int64()),
    ("DowntickVolume", int64()),
    ("RepeatUptickVolume", int64()),
    ("RepeatDowntickVolume", int64()),
    ("UnknownTickVolume", int64()),
    ("TradeToMidVolWeight", float64()),
    ("TradeToMidVolWeightRelative", float64()),
    ("TimeWeightBid", float64()),
    ("TimeWeightAsk", float64()),
    ("secid", int64())])
