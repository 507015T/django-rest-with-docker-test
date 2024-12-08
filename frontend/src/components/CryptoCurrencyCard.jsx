import { Card } from 'antd';
import numberWithCommas from "../utils.js";
function CryptoCurrencyCard(props) {
  const { currency } = props 
  const formattedMarketCap = numberWithCommas(Math.round(currency.quote.USD.market_cap))
  const priceChangeColor = currency.quote.USD.percent_change_24h > 0 ? 'text-green-400' : 'text-red-400'
  // Логируем данные, которые приходят в компонент
  //console.log("CryptoCurrencyCard received currency:", currency.id);
  return (
    <div>
        <Card
          title={
                    <div className="flex items-center gap-3">
                        <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`} alt="" width="50"/>
                        <p className="text-2xl">{currency.name}</p>
                    </div>
                }
          style={{
            width: 700,
            height: 340,
            'box-shadow': '0 3px 10px rgb(0,0,0,0.2)',
          }}
          className="text-2xl"
        >
        <div>
              <p className="m-2">Price : {currency.quote.USD.price}$</p>
              <p className="m-2 mt-4">Price change in 24 hours: <span className={priceChangeColor}>{currency.quote.USD.percent_change_24h}%</span></p>
              <p className="m-2 mt-4">Current capitalization: ${formattedMarketCap}</p>
        </div>
        </Card>
    </div>
  )
}

export default CryptoCurrencyCard
