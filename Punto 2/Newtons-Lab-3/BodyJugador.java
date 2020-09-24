import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class BodyJugador here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class BodyJugador extends Body
{
    public BodyJugador(int size, double mass, Vector velocity, Color color) {
        super(size, mass, velocity, color);
    }
    
    /**
     * Act - do whatever the BodyJugador wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        super.applyForces();
        move();
        bounceAtEdge();
        checkKeyPressed();            
    }    
    
    public void checkKeyPressed() {
        if (Greenfoot.isKeyDown("left")) {
            int direction = velocity.getDirection();
            velocity.setDirection(direction - 10);
        } else if (Greenfoot.isKeyDown("right")) {
            int direction = velocity.getDirection();
            velocity.setDirection(direction + 10);
        }
    }
}
