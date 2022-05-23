import React from "react";
import { useState } from "react";

import { useNavigate } from 'react-router-dom';



//TODO use port and url in json file

export const ValuesIntroduction = () => {
  

  const [checked, setChecked] = useState(false);

  const navigate = useNavigate();

  const handleNext = () => {
    //the navigated page is possibly going to change in the future 
    navigate('/questionnaire')
  }
  const buttonStyleActive = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full";

 

  return (
    <div className='flex flex-col items-center justify-between h-screen w-screen py-28'>
    <h1 className="text-2xl py-5">Introduction values questionnaire </h1>
    <div className="w-1/2 h-3/4 overflow-y-scroll">
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cum, fugit! Accusantium obcaecati voluptatem numquam. Repellat adipisci repudiandae facere nesciunt beatae neque in quibusdam, perspiciatis, quidem quo officiis aperiam inventore, impedit eius sint dolorum aliquam ipsam amet natus asperiores eos aliquid quis! Quidem at deleniti consectetur, dicta praesentium corporis perspiciatis nemo similique sequi amet provident quos laboriosam recusandae eaque quasi aliquam eius aspernatur soluta nisi, non aperiam excepturi? Optio, sint? Et consequatur repudiandae adipisci ab aliquid tempore! Excepturi perspiciatis nobis reiciendis. Voluptatibus deserunt eveniet rerum animi. Eum natus, sit voluptate debitis cumque explicabo ipsum quam quo, quae vel minima in ducimus illo dolores molestiae magnam corporis minus, enim dolorem non! Aut excepturi, expedita reiciendis quis numquam accusamus maiores voluptatem corrupti corporis pariatur recusandae sequi error ad eaque doloribus. Dignissimos corporis a sit velit, repellat hic reiciendis mollitia commodi alias nemo aspernatur rem aliquid corrupti quia animi cum sint tenetur vel provident porro! Nostrum, saepe obcaecati tempore blanditiis magni ad provident suscipit eveniet rerum, neque corrupti sit hic incidunt aliquam, eaque dolorem sed excepturi. Sunt nihil rem saepe voluptas at recusandae deleniti ad facere animi tenetur. Laborum delectus tempore earum sint doloribus, unde iste, accusamus quasi ratione cupiditate fugit modi amet praesentium illum dicta dolores veritatis. Mollitia quis aliquam cum consectetur! Adipisci, exercitationem sint. Excepturi rerum, consectetur facere modi nemo asperiores aut aliquam quo reprehenderit aspernatur nam voluptate, ex veritatis, cupiditate qui nulla mollitia? Repudiandae, dicta officia doloribus voluptatem ratione quo repellat sint nesciunt tenetur dolor illo atque porro, commodi facilis quod, pariatur labore! Perferendis optio est nisi, id tempore aliquam reprehenderit numquam repellat debitis possimus. Aut facilis corrupti aspernatur fugit voluptate consequuntur iure ab. Itaque natus assumenda, aperiam voluptatum dicta eligendi voluptatem ullam nemo consequuntur tempore suscipit nostrum beatae soluta, eos temporibus enim incidunt consectetur maxime ipsum! Assumenda porro officiis repellendus at tempora, officia amet facilis sed eveniet beatae voluptatibus, culpa quibusdam qui tempore maxime voluptatem consequatur praesentium corrupti? Ratione accusamus iusto voluptatibus ipsam. Officiis corporis qui possimus unde fugit laborum in, optio dolores. Doloremque aspernatur odit suscipit aperiam optio provident doloribus temporibus obcaecati dolores vitae facere voluptates unde error nobis ducimus quis est, atque deserunt porro sed non itaque incidunt voluptas consequatur? Minus neque ex facilis ipsa. Aspernatur alias nisi enim quisquam? Quaerat, alias corrupti! Perspiciatis ut architecto, aperiam dolore pariatur doloribus voluptatem magni, voluptatibus voluptate quisquam, rem saepe dolorum. Blanditiis, deserunt dolore nobis autem illo fugiat quam quas aliquam vero aperiam! Asperiores laboriosam laudantium porro possimus iusto. Libero, magni accusantium. Harum molestiae modi atque nesciunt corrupti voluptatum animi iusto officiis nihil fuga nemo in fugit, perferendis amet debitis porro beatae nam vitae? Ipsa nostrum pariatur, quo mollitia illo nobis quas asperiores commodi nesciunt voluptatum reiciendis doloribus neque voluptate obcaecati, maiores adipisci perferendis provident magni odit expedita soluta eligendi suscipit. Reprehenderit possimus ab doloremque repudiandae nam mollitia, quod quisquam praesentium fugit repellat sint consectetur voluptates ad cumque sed ex minima sit aliquam! Cumque, corrupti iste odio, cum omnis aliquid rerum cupiditate soluta perspiciatis, voluptatum sunt ratione qui. Perspiciatis, quasi maxime?</p>
    </div>
    <div className="flex items-center justify-center w-fit mb-5 space-x-7 py-10">
      <button className={buttonStyleActive} onClick={handleNext} >
        <div className='grid place-items-center '>
          <span className="text-white"> next </span>
        </div>
      </button> 
    </div>
  </div>
  )
}