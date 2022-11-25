`#love_box`

## The original vision:  

> An `MicroPython` attempt to create something small, lovely and useful...! :"}  
> ```js
>  __________
> | ________ | // - It's a Pico W
> || Lovely || // - With two buttons
> || #Texts || //   - `x` for `#Xiss`
> ||________|| //   - `o` for `#Okay`
> |   x  o   |
> |__________|
> 
> /* The Screen is for lovely texts stored somewhere,  
> on the blockchain...? */
> ```

## Reality:

A robot with 02 wheels...!

### TODOs:
- [ ] Async web server, currenly the server loop blocks everything
- [ ] Try out controllin' motors

### DONEs:
- [x] Try [uasyncio](https://docs.micropython.org/en/v1.19.1/library/uasyncio.html?highlight=uasyncio)
- [x] Power it - just use the GPIO pins
- [x] Host AP for signing into APs
- [x] fetch & store APs
- [x] `kv_db`
- [x] Join new APs - ___how about hosting your own AP when NOT connected___...?
- [x] Caching mechanism for *lovely texts* - [btree](https://docs.micropython.org/en/latest/library/btree.html)...!
- [x] Not having a Pico W...!
- [x] ~~`Rust` or~~ `Python` - much more easier, also to learn...?
