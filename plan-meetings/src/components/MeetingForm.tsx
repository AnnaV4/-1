// src/components/MeetingForm.tsx
import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap'
import { format, parseISO } from 'date-fns'

interface Meeting {
  title: string
  startTime: Date
  endTime: Date
}

const MeetingForm = () => {
  const [title, setTitle] = useState('')
  const [startTime, setStartTime] = useState(new Date())
  const [endTime, setEndTime] = useState(new Date())

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault()
    console.log({ title, startTime, endTime })
    // Здесь можно добавить логику отправки данных на сервер
  }

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formTitle">
        <Form.Label>Название встречи</Form.Label>
        <Form.Control type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
      </Form.Group>

      <Form.Group controlId="formStartTime">
        <Form.Label>Начало встречи</Form.Label>
        <Form.Control type="datetime-local" value={format(startTime, 'yyyy-MM-ddTHH:mm')} onChange={(e) => setStartTime(parseISO(e.target.value))} />
      </Form.Group>

      <Form.Group controlId="formEndTime">
        <Form.Label>Конец встречи</Form.Label>
        <Form.Control type="datetime-local" value={format(endTime, 'yyyy-MM-ddTHH:mm')} onChange={(e) => setEndTime(parseISO(e.target.value))} />
      </Form.Group>

      <Button variant="primary" type="submit">Создать встречу</Button>
    </Form>
  )
}

export default MeetingForm