import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import correctLogo from '../../assets/correctLogo.svg'
import { thanksPageSecurity } from "../../controller/pathSecurityController";

export const Thanks = () => {

  const navigate = useNavigate()

  useEffect(() => {
    thanksPageSecurity(navigate)

  }, []);

  return (
    <div className='flex flex-col items-center justify-center h-screen w-screen text-center'>
      <h3 className="text-4xl pd-5">THANK YOU</h3>
      <img src={correctLogo} alt="correct Logo" className="fill-white h-20" />
      <h2 className="p-10 text-xl font-semibold">Congratulations! You have reached the end of the survey. Thank you for completing it! Your completion code to enter into Prolific to validate your participations and get your compensation is : </h2>
      <br />
      <span className="font-bold text-2xl pb-8">k8cd2w</span>
      <p className="w-3/5">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem qui consectetur quas dolor eos aspernatur molestias, deleniti impedit aperiam illo delectus vero velit praesentium. Corrupti amet consectetur saepe consequatur commodi ad neque, quia quis nobis aut necessitatibus pariatur nesciunt animi molestias explicabo assumenda. Iste quis modi a? Natus dicta cum temporibus eos eum sunt et, magnam, minus corporis quia, nam eius consequatur dolorem recusandae sapiente vero? Ea, illo veniam. Quo, nisi quos! Quae reprehenderit magni tempora perspiciatis, molestiae, animi quidem ipsam natus minus quod aliquid! In perspiciatis nesciunt provident, adipisci est facilis cum dignissimos repudiandae esse natus ex eveniet deleniti.</p>
      
    </div>
  )
}