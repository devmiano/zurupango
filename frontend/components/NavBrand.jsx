import React from "react";
import logo from "../assets/icons/logo-mask.svg";
import Image from "next/image";

const NavBrand = () => {
  return (
    <a href="/" id="navbrand">
      <div className="logo">
        <Image className="img" src={logo} alt="logo" />
      </div>
    </a>
  );
};

export default NavBrand;
