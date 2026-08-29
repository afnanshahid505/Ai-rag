import { useState,useEffect } from 'react'
import { getInterviewquestions } from './services/interviewApi'


import './App.css'

function App() {
 const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  useEffect(()=>{
    const loadingquestions=async()=>{
      try{
        const data= await getInterviewquestions();
        console.log("api response",data)
        setQuestions(data.questions || [])
      }
      catch(err){
        console.log(err)
        setError("failed to load the questions")

      }
      finally{
        setLoading(false)
      }
    };
    loadingquestions();

  },[]);
  if(loading){
    return <h1>Generating questions...</h1>
  }
    if (error) {
    return <h2>{error}</h2>;
  }

  return (
    <>
    <h1>Ai interview </h1>
    {questions.map((item)=>{
      <div key={item.id}>
        <p>{item.topic}</p>
        <h3>{item.question}</h3>
      </div>
    })}      
    </>
  )
}

export default App
