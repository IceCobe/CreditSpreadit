import { useState } from 'react'
import { useFetch } from '../hooks/useFetch'
import './CreditList.css'

export default function CreditList() {
    const [url, setUrl] = useState('http://127.0.0.1:8000/api/creditspreadit/')
    const { data: creditcards } = useFetch(url)

    return (
        <div className="credit-list">
            <h2>CreditCard List</h2>
            <ul>
                {creditcards.map(card => (
                <li key={card.id}>
                    <h3>{card.name}</h3>
                    <p>{card.company}</p>
                </li>
                ))}
            </ul>
        </div>
    )
}