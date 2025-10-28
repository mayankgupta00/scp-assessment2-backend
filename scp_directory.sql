-- Create Database
CREATE DATABASE IF NOT EXISTS scp_directory;
USE scp_directory;

-- Create Table
CREATE TABLE scp_subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(50) NOT NULL,
    class VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    containment TEXT NOT NULL
);

-- Insert 20 SCP Records
INSERT INTO scp_subjects (item, class, description, containment) VALUES
('SCP-001', 'Euclid', 'A sentient entity claiming to be the guardian of the SCP universe.', 'Kept under digital encryption, only Level-5 personnel may access.'),
('SCP-002', 'Euclid', 'A large organic structure resembling an apartment.', 'Contain in isolated hangar with full quarantine protocols.'),
('SCP-003', 'Safe', 'An organic computer component capable of generating biological material.', 'Maintain constant power; temperature must not drop below 35°C.'),
('SCP-004', 'Euclid', '12 rusted keys and a door that lead to alternate dimensions.', 'Keys stored separately; door sealed in concrete chamber.'),
('SCP-005', 'Safe', 'A key capable of unlocking any lock.', 'Keep in secure locker; Level-2 authorization required for testing.'),
('SCP-006', 'Safe', 'A small spring of water granting regeneration properties.', 'Protected facility; no direct human consumption allowed.'),
('SCP-007', 'Euclid', 'A man with a miniature planet inside his abdomen.', 'Monitored in comfort suite; no medical intervention allowed.'),
('SCP-008', 'Euclid', 'A prion that causes zombification.', 'Stored in Bio-Containment Zone-4; full hazmat suits mandatory.'),
('SCP-009', 'Euclid', 'A substance resembling red ice that freezes at -100°C.', 'Contain in cryogenic chamber at -120°C; no contact with water.'),
('SCP-010', 'Safe', 'A set of collars controlling wearer’s actions.', 'Kept in sealed locker; testing authorized only with D-class subjects.'),
('SCP-011', 'Safe', 'An animate Civil War-era statue that fires muskets.', 'Regular maintenance; monument monitored via CCTV.'),
('SCP-012', 'Euclid', 'A music sheet that compels subjects to use their own blood as ink.', 'Keep sealed in reinforced glass; gloves required for handling. '),
('SCP-013', 'Safe', 'A pack of blue cigarettes that alter user’s perception.', 'Contain in standard safe; no smoking permitted.'),
('SCP-014', 'Safe', 'A man who does not age or move.', 'Monitor vitals weekly; held in medical observation chamber.'),
('SCP-015', 'Euclid', 'A network of pipes that grow uncontrollably.', 'Area sealed; inspection via drones only.'),
('SCP-016', 'Keter', 'A blood-borne pathogen that adapts lethally to environment.', 'Bio-Containment Zone-5; all personnel vaccinated and quarantined.'),
('SCP-017', 'Keter', 'A humanoid shadow that devours light and life.', 'Kept in lighted glass cube; no shadows allowed near containment.'),
('SCP-018', 'Euclid', 'A red rubber ball that accelerates with every bounce.', 'Store in steel-lined room; release only under supervision.'),
('SCP-019', 'Keter', 'A ceramic jar spawning hostile entities.', 'Seal jar lid with industrial adhesive; containment cell under heavy lockdown.'),
('SCP-020', 'Keter', 'A mold that spreads by altering human perception.', 'Keep in darkness; visual feed via remote sensors only.');
