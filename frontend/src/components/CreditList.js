import { PureComponent, useState } from 'react'
import { useFetch } from '../hooks/useFetch'
import './CreditList.css'

export default function CreditList() {
  const [url, setUrl] = useState('http://127.0.0.1:8000/api/creditspreadit/')
  const { data: creditcards } = useFetch(url)

  console.log(creditcards)

  return (
    <div className="credit-list">
      <h2>CreditCard List</h2>
      <ul>
        {creditcards && creditcards.map(card => (
        <li key={card.id}>
          <h3>{card.name}</h3>
          <p>{card.company}</p>
          {card.bonuses.map(bonus => (
            <li key={bonus.id}>
              <p>{bonus}</p>
            </li>
          ))}
        </li>
        ))}
      </ul>
    </div>
  )
}