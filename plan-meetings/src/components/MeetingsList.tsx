// src/components/MeetingsList.tsx
import React, { useState } from 'react'
import { Table } from 'react-bootstrap'
import { format } from 'date-fns'

interface Meeting {
  id: number
  title: string
  startTime: Date
  endTime: Date
}

const MeetingsList = () => {
  const [meetings, setMeetings] = useState<Meeting[]>([])

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Название</th>
          <th>Начало</th>
          <th>Конец</th>
        </tr>
      </thead>
      <tbody>
        {meetings.map((meeting, index) => (
          <tr key={meeting.id}>
            <td>{index + 1}</td>
            <td>{meeting.title}</td>
            <td>{format(meeting.startTime, 'dd.MM.yyyy HH:mm')}</td>
            <td>{format(meeting.endTime, 'dd.MM.yyyy HH:mm')}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  )
}

export default MeetingsList