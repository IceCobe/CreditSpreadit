import { useState } from 'react'
import { useFetch } from '../hooks/useFetch'
import './CreditList.css'

export default function TripList() {
    const [url, setUrl] = useState('http://localhost:3000/credit')
    const { data: creditcard } = useFetch(url)

    return (
        <div className="trip-list">
            <h2>CreditCard List</h2>
            <ul>
                {credit && creditcard.map(card => (
                <li key={card.id}>
                    <h3>{card.title}</h3>
                    <p>{card.price}</p>
                </li>
                ))}
            </ul>
            <div className="filters">
                <button onClick={() => setUrl('http://localhost:3000/cardss?company=Discover')}>
                Discover Cards
                </button>
                <button onClick={() => setUrl('http://localhost:3000/cards')}>
                All Cards
                </button>
            </div>
        </div>
    )
}