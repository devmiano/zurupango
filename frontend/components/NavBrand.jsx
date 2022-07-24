import React from "react";
import logo from "../assets/icons/logo-mask.svg";
import Image from "next/image";

const NavBrand = () => {
  return (
    <a href="/" id="navbrand">
      <Image className="logo" src={logo} alt="logo" />
    </a>
  );
};

export default NavBrand;
