push=require 'push'
Class=require 'class'
require 'Ball'
require 'Paddle'





WINDOW_HEIGHT=720
WINDOW_WIDTH=1280



VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243

PADDLE_SPEED = 200

player1Y=30
player1Score=0
player1Beep = love.audio.newSource('player1.wav',wav)
player1WinBeep = love.audio.newSource('player1win.wav',wav)

player2Y=VIRTUAL_HEIGHT-50
player2Score=0
player2Beep = love.audio.newSource('player2.wav',wav)
player2WinBeep = love.audio.newSource('player2win.wav',wav)

winSound=0
scoreSound = love.audio.newSource('scored.wav',wav)
wallHitSound = love.audio.newSource('wallHit.wav',wav)

function love.load()
    math.randomseed(os.time())
    
    love.graphics.setDefaultFilter('nearest','nearest')

    smallFont = love.graphics.newFont('font.ttf',8)
    love.graphics.setFont(smallFont)
    scoreFont = love.graphics.newFont('font.ttf',32)

    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
})
    
    player1Score=0
    player2Score=0

    player1=Paddle(10,30,5,20)
    player2=Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT/2-2,5,20)

    ball=Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

    servingPlayer=1
    gameState='start'

end

function love.update(dt)
    if love.keyboard.isDown('w') then
        player1.dy=-PADDLE_SPEED
    elseif love.keyboard.isDown('s') then
        player1.dy=PADDLE_SPEED
    else
        player1.dy=0
    end

    if love.keyboard.isDown('i') then
        player2.dy=-PADDLE_SPEED
    elseif love.keyboard.isDown('k') then
        player2.dy=PADDLE_SPEED
    else
        player2.dy=0
    end

    if gameState == 'play' then
        if ball:collides(player1) then
            ball.dx = -ball.dx*1.03
            ball.x = player1.x+5
            love.audio.play(player1Beep)
            if ball.dy<0 then
                ball.dy = -math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
        end
        if ball:collides(player2) then
            ball.dx = -ball.dx*1.03
            ball.x = player2.x-5
            love.audio.play(player2Beep)
            if ball.dy<0 then
                ball.dy = -math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
        end

        if ball.y <= 0 then
            ball.y=0
            ball.dy = -ball.dy
            love.audio.play(wallHitSound)
        end
        if ball.y>=VIRTUAL_HEIGHT-4 then
            ball.y=VIRTUAL_HEIGHT-4
            ball.dy=-ball.dy
            love.audio.play(wallHitSound)
        end
        ball:update(dt)
    end

    if gameState=='serve' then
        if servingPlayer==1 then
            ball.dx=math.random(140,200)
        elseif servingPlayer==2 then
            ball.dx=-math.random(140,200)
        end
    end

    if gameState=='win' then
        ball.dx=0
        ball.dy=0
        ball:reset()
        if winSound==0 then
            if winningPlayer==1 then
                love.audio.play(player1WinBeep)
                winSound=1
            elseif winningPlayer==2 then
                love.audio.play(player2WinBeep)
                winSound=1
            end
        end
    end

    if ball.x<0 then
        player2Score=player2Score+1
        if player2Score<10 then
            love.audio.play(scoreSound)
        end
        ball:reset()
        servingPlayer=2
        gameState='serve'
    end

    if ball.x>VIRTUAL_WIDTH then
        player1Score=player1Score+1
        if player1Score<10 then
            love.audio.play(scoreSound)
        end
        ball:reset()
        servingPlayer=1
        gameState='serve'
    end

    if player1Score>=10 then
        winningPlayer=1
        gameState='win'
    elseif player2Score>=10 then
        winningPlayer=2
        gameState='win'
    end


    player1:update(dt)
    player2:update(dt)

end
    
    
function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key=='space' or key=='enter' or key=='return' then
        if gameState=='start' or gameState=='serve' then
            gameState = 'play'
        else
            gameState='start'
            Ball:reset()
        end
    elseif key == 'delete' then
        gameState='start'
        player1Score=0
        player2Score=0
        winSound=0
        ball:reset()
    end
end


function love.draw()
    push:apply('start')

    love.graphics.clear(40,45,52,255)
    love.graphics.setFont(smallFont)

    if gameState == 'start' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Space to Begin!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'serve' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s Serve!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Space to Serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'win' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(winningPlayer) .. " Wins!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Delete to Serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        -- no UI messages to display in play
    end

    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)

    player1:render()
    player2:render()

    ball:render()

    displayFPS()

    push:apply('end')
end

function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end