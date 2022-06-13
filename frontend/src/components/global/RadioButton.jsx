const inputStyle = "appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mx-1 cursor-pointer";

export const RadioButton = (props) => {

  const {
    answers, //Map containing questionnaire answers
    value, //Number : Value of the current radio button (if it's the first it'll be 1 and so on...)
    questionNumber, //Number : question number
    onChange, //Function that triggers when an answer is changed
    type //?String, can be either 'personality', 'values' or undefined.
  } = props;

  return (
    <div className="flex flex-col items-center">
      {type === 'values' 
        ? <label className="" htmlFor={`${questionNumber}${type}${value}`}>{value}</label>
        : ""
      }
      <input 
        type="radio" 
        className={inputStyle} 
        value={value}
        id={`${questionNumber}${type}${value}`}
        name={`${questionNumber}${type}`}
        onChange={e => onChange(e, questionNumber)}
        defaultChecked={answers.get(questionNumber + 1) === value}
      /> 
    </div>
  )
}