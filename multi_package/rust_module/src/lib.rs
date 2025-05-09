#![crate_type = "cdylib"]

use std::os::raw::c_int;

#[no_mangle]
pub extern "C" fn add_numbers(a: c_int, b: c_int) -> c_int {
    a + b
}

#[no_mangle]
pub extern "C" fn rust_greeting(name: *const std::os::raw::c_char) -> *const std::os::raw::c_char {
    let c_str = unsafe { std::ffi::CStr::from_ptr(name) };
    let name = c_str.to_str().unwrap();
    let greeting = format!("Hello from Rust, {}!", name);
    std::ffi::CString::new(greeting).unwrap().into_raw()
}